// Main JavaScript for HK Exports

document.addEventListener('DOMContentLoaded', function() {
    // Auto-hide alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        if (!alert.classList.contains('alert-info')) {
            setTimeout(() => {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            }, 5000);
        }
    });

    // Form validation
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // Basic validation already in HTML5
        });
    });
});

// Utility function to format currency
function formatCurrency(value) {
    return new Intl.NumberFormat('en-BD', {
        style: 'currency',
        currency: 'BDT'
    }).format(value);
}
