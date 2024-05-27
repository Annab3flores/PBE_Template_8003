document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('empregado-form');
    const empregadosLista = document.getElementById('empregados-lista');
    const formTitle = document.getElementById('form-title');
    const submitButton = document.getElementById('submit-button');
    const cancelButton = document.getElementById('cancel-button');
    const empregadoIdInput = document.getElementById('empregado-id');

    const API_URL = 'http://127.0.0.1:8000/api/empregados/'; // Substitua pelo endereço correto da sua API

    async function fetchEmpregados() {
        const response = await fetch(API_URL);
        const empregados = await response.json();
        empregadosLista.innerHTML = '';
        empregados.forEach(empregado => {
            const li = document.createElement('li');
            li.innerHTML = `
                ${empregado.nome} ${empregado.sobrenome} - ${empregado.cargo} 
                <button onclick="editEmpregado(${empregado.id})">Editar</button>
                <button onclick="deleteEmpregado(${empregado.id})">Deletar</button>
            `;
            empregadosLista.appendChild(li);
        });
    }

    async function addOrUpdateEmpregado(event) {
        event.preventDefault();
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);
        const empregadoId = empregadoIdInput.value;

        const method = empregadoId ? 'PUT' : 'POST';
        const url = empregadoId ? `${API_URL}${empregadoId}/` : API_URL;

        const response = await fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });

        if (response.ok) {
            fetchEmpregados();
            form.reset();
            resetForm();
        }
    }

    async function editEmpregado(id) {
        const response = await fetch(`${API_URL}${id}/`);
        if (response.ok) {
            const empregado = await response.json();
            empregadoIdInput.value = empregado.id;
            document.getElementById('nome').value = empregado.nome;
            document.getElementById('sobrenome').value = empregado.sobrenome;
            document.getElementById('email').value = empregado.email;
            document.getElementById('telefone').value = empregado.telefone;
            document.getElementById('cargo').value = empregado.cargo;
            document.getElementById('data_contratacao').value = empregado.data_contratacao;

            formTitle.textContent = 'Editar Empregado';
            submitButton.textContent = 'Atualizar';
            cancelButton.style.display = 'inline';
        }
    }

    async function deleteEmpregado(id) {
        const response = await fetch(`${API_URL}${id}/`, {
            method: 'DELETE',
        });
        if (response.ok) {
            fetchEmpregados();
        }
    }

    function resetForm() {
        empregadoIdInput.value = '';
        formTitle.textContent = 'Adicionar Empregado';
        submitButton.textContent = 'Adicionar';
        cancelButton.style.display = 'none';
    }

    form.addEventListener('submit', addOrUpdateEmpregado);
    cancelButton.addEventListener('click', () => {
        form.reset();
        resetForm();
    });

    window.editEmpregado = editEmpregado;
    window.deleteEmpregado = deleteEmpregado;

    fetchEmpregados();
});
