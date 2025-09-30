document.addEventListener("DOMContentLoaded", function() {

    
    // Pega o elemento boty e o valor do atributo data-open-target para ver se deve abrir o offcanvas
    const bodyElement = document.body;
    const openTarget = bodyElement.dataset.openTarget;
    
    // Pega o offcanvas e o número de resultados
    const offcanvas = new bootstrap.Offcanvas(document.getElementById('searchBackdrop'));
   // let num_results_text = document.getElementById("num_results_id").innerText;
    
    
    // Abre o canvas de cara, caso o usuário venha da pesquisa
    if (openTarget === 'searchBackdrop')
        offcanvas.show();

    // Abre o canvas caso não tenha resultados;
    //if (num_results_text == "Nenhum registro foi encontrado")
    //    offcanvas.show();

    // Pega todos os campos do formulário
    const fields = document.querySelectorAll('.field-onchange');
    const submitButton = document.getElementById('btn_search');
    let changedField = false;

    //Percorre os campos para ver se houve mudanças

    fields.forEach(field => {

        field.addEventListener('change', function() {
            changedField = true;
            checkChanges();
        });
    
        if (field.type === 'text') {
            field.addEventListener('input', function() {
                changedField = true;    
                checkChanges();
            });
        }
    });

    function checkChanges() {
        submitButton.disabled = !changedField;
    }
});

