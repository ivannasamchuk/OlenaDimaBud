function changeLanguage(lang) {
    document.querySelectorAll('[data-ua], [data-pl], [data-en]').forEach(function(element) {
        if (element.hasAttribute('data-' + lang)) {
            element.innerText = element.getAttribute('data-' + lang);
        }
    });
}
