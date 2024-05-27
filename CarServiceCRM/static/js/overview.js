document.addEventListener('DOMContentLoaded', function () {
    // Функция для переключения вкладок на основе фрагмента URL
    function switchTabFromURL() {
        const hash = window.location.hash;
        if (hash) {
            const tab = document.querySelector(`[data-bs-target="${hash}"]`);
            if (tab) {
                const tabInstance = new bootstrap.Tab(tab);
                tabInstance.show();
            }
        }
    }

    // Обновление URL при переключении вкладок
    const tabs = document.querySelectorAll('#myTab button[data-tab]');
    tabs.forEach(tab => {
        tab.addEventListener('shown.bs.tab', function (event) {
            const target = event.target.getAttribute('data-bs-target');
            if (target) {
                history.replaceState(null, null, target);
            }
        });
    });

    // Переключение вкладок при загрузке страницы
    switchTabFromURL();

    // Переключение вкладок при изменении фрагмента URL вручную
    window.addEventListener('hashchange', switchTabFromURL);
});