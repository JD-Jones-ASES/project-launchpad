/* app.js — Scholastica Codex shared client-side logic */

/* ═══════════════════════════════════════════════════════════
   Catalog Page: renderCatalog()
   ═══════════════════════════════════════════════════════════ */

var catalogData = null;
var activeCategory = 'all';
var activeLevel = 'all';

function renderCatalog(data) {
    catalogData = data;
    buildFilterPills(data);
    renderCourseGrid(data);

    // "All" buttons (static in HTML)
    document.querySelectorAll('.filter-pill[data-value="all"]').forEach(function(pill) {
        pill.addEventListener('click', function() {
            var filterType = pill.getAttribute('data-filter');
            if (filterType === 'category') filterCategory('all');
            else if (filterType === 'level') filterLevel('all');
        });
    });

    // Search input
    var searchInput = document.getElementById('search-input');
    if (searchInput) {
        searchInput.addEventListener('input', function() {
            renderCourseGrid(catalogData);
        });
    }
}

function buildFilterPills(data) {
    // Category pills
    var catContainer = document.getElementById('category-pills');
    if (catContainer) {
        var seen = {};
        data.sections.forEach(function(section) {
            if (!seen[section.id]) {
                seen[section.id] = true;
                var btn = document.createElement('button');
                btn.className = 'filter-pill';
                btn.setAttribute('data-filter', 'category');
                btn.setAttribute('data-value', section.id);
                btn.textContent = section.title;
                btn.addEventListener('click', function() { filterCategory(section.id); });
                catContainer.appendChild(btn);
            }
        });
    }

    // Level pills — collect unique levels
    var levelContainer = document.getElementById('level-pills');
    if (levelContainer) {
        var levels = {};
        data.sections.forEach(function(section) {
            section.courses.forEach(function(c) {
                levels[c.level] = true;
            });
        });
        Object.keys(levels).sort().forEach(function(level) {
            var btn = document.createElement('button');
            btn.className = 'filter-pill';
            btn.setAttribute('data-filter', 'level');
            btn.setAttribute('data-value', level);
            btn.textContent = level;
            btn.addEventListener('click', function() { filterLevel(level); });
            levelContainer.appendChild(btn);
        });
    }
}

function filterCategory(catId) {
    activeCategory = catId;
    updatePillStates('category', catId);
    renderCourseGrid(catalogData);
}

function filterLevel(level) {
    activeLevel = level;
    updatePillStates('level', level);
    renderCourseGrid(catalogData);
}

function updatePillStates(filterType, value) {
    document.querySelectorAll('.filter-pill[data-filter="' + filterType + '"]').forEach(function(pill) {
        pill.classList.remove('active');
        if (pill.getAttribute('data-value') === value) {
            pill.classList.add('active');
        }
    });
    // Also handle the "All" pill
    document.querySelectorAll('.filter-pill[data-filter="' + filterType + '"][data-value="all"]').forEach(function(pill) {
        if (value === 'all') pill.classList.add('active');
        else pill.classList.remove('active');
    });
}

function renderCourseGrid(data) {
    var grid = document.getElementById('catalog-grid');
    if (!grid) return;

    var searchQuery = '';
    var searchInput = document.getElementById('search-input');
    if (searchInput) searchQuery = searchInput.value.toLowerCase().trim();

    var html = '';
    var shown = 0;

    data.sections.forEach(function(section) {
        if (activeCategory !== 'all' && section.id !== activeCategory) return;

        section.courses.forEach(function(course) {
            if (activeLevel !== 'all' && course.level !== activeLevel) return;

            if (searchQuery) {
                var searchable = (course.title + ' ' + course.desc).toLowerCase();
                if (searchable.indexOf(searchQuery) === -1) return;
            }

            var badges = [];
            if (course.quiz_count > 0) badges.push(course.quiz_count + ' quizzes');
            if (course.guide_count > 0) badges.push(course.guide_count + ' guides');
            if (course.has_playlist) badges.push('videos');
            if (course.has_cyoa) badges.push('CYOA');

            html += '<a href="courses/' + course.project_id + '.html" class="catalog-card">';
            html += '<span class="catalog-badge">' + escapeHtml(course.level) + '</span>';
            html += '<h3 class="catalog-title">' + escapeHtml(course.title) + '</h3>';
            html += '<p class="catalog-desc">' + escapeHtml(course.desc) + '</p>';
            html += '<div class="catalog-meta">';
            html += '<span class="catalog-sections">' + course.section_count + ' sections</span>';
            if (badges.length > 0) {
                html += '<span class="catalog-assets">' + badges.join(' &middot; ') + '</span>';
            }
            html += '</div>';
            html += '</a>';
            shown++;
        });
    });

    if (shown === 0) {
        html = '<p class="catalog-empty">No courses match your filters.</p>';
    }

    grid.innerHTML = html;
}


/* ═══════════════════════════════════════════════════════════
   Course Page: renderCoursePage()
   ═══════════════════════════════════════════════════════════ */

function renderCoursePage(data) {
    // Pre-load sonnet data if available (Shakespeare_Sonnets)
    if (data.sonnet_data) {
        sonnetData = data.sonnet_data;
    }

    // Fill in header details
    var levelEl = document.getElementById('course-level');
    if (levelEl) levelEl.textContent = data.level;

    var descEl = document.getElementById('course-desc');
    if (descEl) descEl.textContent = data.desc;

    // Action buttons
    var actionsEl = document.getElementById('course-actions');
    if (actionsEl) {
        var html = '';
        if (data.textbook_url) {
            html += '<a href="../' + data.textbook_url + '" class="course-btn read" download>&#128214; Textbook</a>';
        }
        if (data.teacher_zip) {
            html += '<a href="../' + data.teacher_zip + '" class="course-btn teacher" download>&#128218; Teacher Edition</a>';
        }
        if (data.workbook_zip) {
            html += '<a href="../' + data.workbook_zip + '" class="course-btn workbook" download>&#128221; Workbook</a>';
        }
        if (data.playlist_url) {
            html += '<a href="' + data.playlist_url + '" target="_blank" class="course-btn watch">&#127909; Playlist</a>';
        }
        if (data.cyoa) {
            data.cyoa.forEach(function(cyoa) {
                html += '<a href="../Interactives/' + cyoa.id + '/index.html" target="_blank" class="course-btn cyoa">&#128218; ' + escapeHtml(cyoa.title || 'Adventure') + '</a>';
            });
        }
        actionsEl.innerHTML = html;
    }

    // Section table
    var tableEl = document.getElementById('course-table');
    if (tableEl && data.sections && data.sections.length > 0) {
        var columns = data.columns || ['quiz', 'guide', 'cards', 'slides', 'maps', 'info'];
        var columnHeaders = {
            quiz: 'Quiz', guide: 'Guide', cards: 'Cards',
            slides: 'Slides', maps: 'Maps', info: 'Info',
            sonnet_popup: 'Sonnet'
        };

        var html = '<table class="quiz-table">';
        html += '<thead><tr><th>Section</th><th>Questions</th>';
        columns.forEach(function(col) {
            html += '<th>' + (columnHeaders[col] || col) + '</th>';
        });
        html += '</tr></thead><tbody>';

        data.sections.forEach(function(s) {
            html += '<tr class="quiz-row">';
            html += '<td class="quiz-name">' + escapeHtml(s.name) + '</td>';

            if (s.question_count > 0) {
                html += '<td class="quiz-count">' + s.question_count + ' questions</td>';
            } else {
                html += '<td class="quiz-count quiz-empty">--</td>';
            }

            columns.forEach(function(col) {
                html += renderColumnCell(col, s, data.project_id);
            });

            html += '</tr>';
        });

        html += '</tbody></table>';
        tableEl.innerHTML = html;

        // Typeset MathJax if loaded
        if (window.MathJax && MathJax.typesetPromise) {
            MathJax.typesetPromise();
        }
    } else if (tableEl) {
        tableEl.innerHTML = '<p class="quiz-coming-soon">Content for this course is being generated. Check back soon.</p>';
    }
}

function renderColumnCell(col, section, pid) {
    var sk = section.key;

    if (col === 'quiz') {
        if (section.has_quiz && section.question_count > 0) {
            return '<td class="quiz-action"><a href="../quizzes/' + pid + '/' + sk + '.html" class="quiz-link">Take Quiz &#10132;</a></td>';
        }
        return '<td class="quiz-action"><span class="quiz-pending">--</span></td>';
    }
    if (col === 'guide') {
        if (section.has_guide) {
            return '<td class="quiz-guide"><a href="../guides/' + pid + '/' + sk + '.html" class="guide-link">Guide</a></td>';
        }
        return '<td class="quiz-guide"><span class="guide-pending">--</span></td>';
    }
    if (col === 'cards') {
        if (section.has_flashcards) {
            return '<td class="quiz-flashcards"><a href="../flashcards/' + pid + '/' + sk + '.html" class="fc-link">Cards</a></td>';
        }
        return '<td class="quiz-flashcards"><span class="guide-pending">--</span></td>';
    }
    if (col === 'slides') {
        if (section.has_slides) {
            return '<td class="quiz-slides"><a href="../slides/' + pid + '/' + sk + '.html" class="slides-link">Slides</a></td>';
        }
        return '<td class="quiz-slides"><span class="guide-pending">--</span></td>';
    }
    if (col === 'maps') {
        if (section.has_mindmap) {
            return '<td class="quiz-mindmap"><a href="../mindmaps/' + pid + '/' + sk + '.html" class="mindmap-link">Map</a></td>';
        }
        return '<td class="quiz-mindmap"><span class="guide-pending">--</span></td>';
    }
    if (col === 'info') {
        if (section.has_infographic) {
            return '<td class="quiz-infographic"><a href="../infographics/' + pid + '/' + sk + '.png" class="infographic-link" target="_blank">Info</a></td>';
        }
        return '<td class="quiz-infographic"><span class="guide-pending">--</span></td>';
    }
    if (col === 'sonnet_popup') {
        if (section.sonnet_num) {
            return '<td class="quiz-mindmap"><button class="sonnet-btn" onclick="showSonnet(\'' + sk + '\')">Sonnet</button></td>';
        }
        return '<td class="quiz-mindmap"><span class="guide-pending">--</span></td>';
    }
    return '<td>--</td>';
}


/* ═══════════════════════════════════════════════════════════
   Sonnet Popup (Shakespeare course page)
   ═══════════════════════════════════════════════════════════ */

var sonnetData = null;

function showSonnet(sk) {
    // Lazy-load sonnet data from the course JSON
    if (!sonnetData) {
        // Try to get it from the already-loaded course data
        var scripts = document.querySelectorAll('script');
        // Actually, just re-fetch
        var pid = 'Shakespeare_Sonnets';
        fetch('../data/courses/' + pid + '.json')
            .then(function(r) { return r.json(); })
            .then(function(data) {
                sonnetData = data.sonnet_data || {};
                doShowSonnet(sk);
            });
        return;
    }
    doShowSonnet(sk);
}

function doShowSonnet(sk) {
    var s = sonnetData[sk];
    if (!s) return;
    document.getElementById('sonnet-title').textContent = 'Sonnet ' + s.numeral;
    document.getElementById('sonnet-text').textContent = s.text;
    document.getElementById('sonnet-overlay').classList.add('active');
}

function closeSonnet() {
    var overlay = document.getElementById('sonnet-overlay');
    if (overlay) overlay.classList.remove('active');
}

// Escape key closes sonnet
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') closeSonnet();
});


/* ═══════════════════════════════════════════════════════════
   Utility
   ═══════════════════════════════════════════════════════════ */

function escapeHtml(text) {
    if (!text) return '';
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(text));
    return div.innerHTML;
}
