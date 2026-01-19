// JavaScript pour Task Manager

document.addEventListener('DOMContentLoaded', function() {
    // Initialisation des tooltips Bootstrap
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Initialisation des popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Auto-dismiss des alerts après 5 secondes
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);

    // Confirmation pour les actions critiques
    var confirmLinks = document.querySelectorAll('[data-confirm]');
    confirmLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            var message = this.getAttribute('data-confirm') || 'Êtes-vous sûr de vouloir effectuer cette action ?';
            if (!confirm(message)) {
                e.preventDefault();
            }
        });
    });

    // Gestion des formulaires
    var forms = document.querySelectorAll('form');
    forms.forEach(function(form) {
        form.addEventListener('submit', function() {
            var submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = '<span class="loading"></span> Traitement...';
            }
        });
    });

    // Filtrage des tableaux
    var searchInputs = document.querySelectorAll('.table-search');
    searchInputs.forEach(function(input) {
        input.addEventListener('keyup', function() {
            var filter = this.value.toLowerCase();
            var table = this.closest('.card').querySelector('table');
            var rows = table.querySelectorAll('tbody tr');
            
            rows.forEach(function(row) {
                var text = row.textContent.toLowerCase();
                row.style.display = text.indexOf(filter) > -1 ? '' : 'none';
            });
        });
    });

    // Compteur de caractères pour les textareas
    var textareas = document.querySelectorAll('textarea[data-max-length]');
    textareas.forEach(function(textarea) {
        var maxLength = textarea.getAttribute('data-max-length');
        var counter = document.createElement('div');
        counter.className = 'form-text text-end';
        counter.innerHTML = '<span class="char-count">0</span>/' + maxLength + ' caractères';
        
        textarea.parentNode.appendChild(counter);
        
        textarea.addEventListener('input', function() {
            var count = this.value.length;
            var charCount = this.parentNode.querySelector('.char-count');
            charCount.textContent = count;
            
            if (count > maxLength * 0.9) {
                charCount.className = 'char-count text-warning';
            } else {
                charCount.className = 'char-count';
            }
            
            if (count > maxLength) {
                charCount.className = 'char-count text-danger';
            }
        });
        
        // Déclencher l'événement input pour l'état initial
        textarea.dispatchEvent(new Event('input'));
    });

    // Gestion des dates
    var dateInputs = document.querySelectorAll('input[type="date"]');
    dateInputs.forEach(function(input) {
        // Définir la date minimale sur aujourd'hui pour les dates futures
        if (input.classList.contains('future-date')) {
            var today = new Date().toISOString().split('T')[0];
            input.min = today;
        }
        
        // Définir la date maximale sur aujourd'hui pour les dates passées
        if (input.classList.contains('past-date')) {
            var today = new Date().toISOString().split('T')[0];
            input.max = today;
        }
    });

    // Animation des cartes statistiques
    var statCards = document.querySelectorAll('.card.text-white');
    statCards.forEach(function(card) {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
        });
    });

    // Gestion des onglets avec sauvegarde de l'état
    var tabPanes = document.querySelectorAll('.tab-pane');
    if (tabPanes.length > 0) {
        var activeTab = localStorage.getItem('activeTab');
        if (activeTab) {
            var tabTrigger = document.querySelector('[data-bs-target="' + activeTab + '"]');
            if (tabTrigger) {
                bootstrap.Tab.getInstance(tabTrigger) || new bootstrap.Tab(tabTrigger);
                tabTrigger.click();
            }
        }

        document.querySelectorAll('[data-bs-toggle="tab"]').forEach(function(tab) {
            tab.addEventListener('shown.bs.tab', function (e) {
                localStorage.setItem('activeTab', e.target.getAttribute('data-bs-target'));
            });
        });
    }

    // Fonction pour mettre à jour le temps réel
    function updateClock() {
        var now = new Date();
        var clockElement = document.getElementById('live-clock');
        if (clockElement) {
            clockElement.textContent = now.toLocaleTimeString('fr-FR');
        }
    }

    // Démarrer l'horloge si l'élément existe
    if (document.getElementById('live-clock')) {
        updateClock();
        setInterval(updateClock, 1000);
    }

    // Gestion des modales
    var modals = document.querySelectorAll('.modal');
    modals.forEach(function(modal) {
        modal.addEventListener('shown.bs.modal', function() {
            var input = this.querySelector('input[autofocus]');
            if (input) {
                input.focus();
            }
        });
        
        modal.addEventListener('hidden.bs.modal', function() {
            var form = this.querySelector('form');
            if (form) {
                form.reset();
            }
        });
    });

    // Export des données (fonction utilitaire)
    window.exportTableToCSV = function(filename) {
        var table = document.querySelector('table');
        if (!table) return;

        var csv = [];
        var rows = table.querySelectorAll('tr');
        
        for (var i = 0; i < rows.length; i++) {
            var row = [], cols = rows[i].querySelectorAll('td, th');
            
            for (var j = 0; j < cols.length; j++) {
                // Nettoyer le texte et ajouter aux colonnes
                var text = cols[j].innerText.replace(/(\r\n|\n|\r)/gm, "").replace(/(\s\s)/gm, " ");
                row.push('"' + text + '"');
            }
            
            csv.push(row.join(","));
        }

        // Télécharger le fichier CSV
        var csvFile = new Blob([csv.join("\n")], {type: "text/csv"});
        var downloadLink = document.createElement("a");
        downloadLink.download = filename;
        downloadLink.href = window.URL.createObjectURL(csvFile);
        downloadLink.style.display = "none";
        document.body.appendChild(downloadLink);
        downloadLink.click();
        document.body.removeChild(downloadLink);
    };

    console.log('Task Manager JavaScript chargé avec succès!');
});

// Fonctions utilitaires globales
const TaskManager = {
    // Afficher un toast de notification
    showToast: function(message, type = 'info') {
        const toastContainer = document.getElementById('toast-container') || (function() {
            const container = document.createElement('div');
            container.id = 'toast-container';
            container.className = 'toast-container position-fixed top-0 end-0 p-3';
            container.style.zIndex = '9999';
            document.body.appendChild(container);
            return container;
        })();

        const toastId = 'toast-' + Date.now();
        const toastHtml = `
            <div id="${toastId}" class="toast align-items-center text-bg-${type} border-0" role="alert">
                <div class="d-flex">
                    <div class="toast-body">
                        ${message}
                    </div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
                </div>
            </div>
        `;

        toastContainer.insertAdjacentHTML('beforeend', toastHtml);
        const toastElement = document.getElementById(toastId);
        const toast = new bootstrap.Toast(toastElement);
        toast.show();

        // Nettoyer après la fermeture
        toastElement.addEventListener('hidden.bs.toast', function() {
            this.remove();
        });
    },

    // Formater une date
    formatDate: function(dateString) {
        const options = { year: 'numeric', month: 'long', day: 'numeric' };
        return new Date(dateString).toLocaleDateString('fr-FR', options);
    },

    // Calculer la différence entre deux dates
    dateDiff: function(date1, date2) {
        const diffTime = Math.abs(new Date(date2) - new Date(date1));
        return Math.ceil(diffTime / (1000 * 60 * 60 * 24));
    }
};