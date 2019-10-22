window.onload = function() {

    let sithList = document.getElementById('sith-list');
    let selectBlockForm = document.getElementById('select-block-form');

    // изначальная установка ссылки
    selectBlockForm.action = String(sithList.value) + '/';
    console.log(selectBlockForm.action);
    // изменение ссылки
    window.addEventListener('change', function(e) {
        if (e.target === sithList) {

            selectBlockForm.action = String(sithList.value) + '/';
            console.log(selectBlockForm.action);
        }
    });
}