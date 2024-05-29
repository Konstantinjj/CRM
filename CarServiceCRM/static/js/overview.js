document.addEventListener('DOMContentLoaded', function () {
    const tabs = document.querySelectorAll('#myTab .nav-link');
    tabs.forEach(tab => {
        tab.addEventListener('click', function (event) {
            event.preventDefault();
            const url = new URL(this.href);
            const groupId = url.searchParams.get('group');
            const targetPane = document.querySelector(`#group-${groupId}`);
            if (targetPane) {
                document.querySelectorAll('.tab-pane').forEach(pane => pane.classList.remove('show', 'active'));
                targetPane.classList.add('show', 'active');
                history.replaceState(null, '', this.href);
            }
        });
    });

    const urlParams = new URLSearchParams(window.location.search);
    const group = urlParams.get('group');
    if (group) {
        const activeTab = document.querySelector(`#tab-${group}`);
        if (activeTab) {
            const tabInstance = new bootstrap.Tab(activeTab);
            tabInstance.show();
        }
    }
});