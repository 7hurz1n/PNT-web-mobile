// assets/js/script.js
// Comportamentos de interface do projeto de Registro de Ocorrências.
// Não depende de classes/IDs extras no HTML: trabalha em cima da
// estrutura que já existe nos templates.

document.addEventListener('DOMContentLoaded', function () {
  confirmarExclusao();
  colorirGravidade();
  preencherDataHoraPadrao();
  estadoVazioHistorico();
  aplicarRotulosTabela();
});

/* Pede confirmação antes de seguir num link de exclusão (/deletar/<id>) */
function confirmarExclusao() {
  document.querySelectorAll('a[href*="/deletar/"]').forEach(function (link) {
    link.addEventListener('click', function (event) {
      const confirmar = window.confirm(
        'Tem certeza que deseja excluir esta ocorrência? Essa ação não pode ser desfeita.'
      );
      if (!confirmar) {
        event.preventDefault();
      }
    });
  });
}

/* Colore a célula de "Gravidade" na tabela do histórico (baixa/média/alta) */
function colorirGravidade() {
  const linhas = document.querySelectorAll('table tr');

  linhas.forEach(function (linha) {
    const celulas = linha.querySelectorAll('td');
    if (celulas.length < 4) return; // ignora o cabeçalho (usa <th>, não <td>)

    // Ordem das colunas em historico.html: ID, Ocorrencia, Detalhes, Gravidade...
    const celulaGravidade = celulas[3];
    if (!celulaGravidade) return;

    const valor = celulaGravidade.textContent.trim().toLowerCase();
    const cores = {
      baixa: '#2f9e44',
      media: '#e8a600',
      'média': '#e8a600',
      alta: '#e0433b'
    };

    if (cores[valor]) {
      celulaGravidade.style.backgroundColor = cores[valor];
      celulaGravidade.style.color = '#ffffff';
      celulaGravidade.style.fontWeight = '600';
      celulaGravidade.style.textAlign = 'center';
      celulaGravidade.style.borderRadius = '6px';
      celulaGravidade.style.textTransform = 'capitalize';
    }
  });
}

/* No formulário de registro, sugere a data e a hora atuais quando os campos estão vazios */
function preencherDataHoraPadrao() {
  const campoData = document.querySelector('input[name="dataForm"]');
  const campoHora = document.querySelector('input[name="horaForm"]');

  if (campoData && !campoData.value) {
    campoData.value = new Date().toISOString().split('T')[0];
  }

  if (campoHora && !campoHora.value) {
    const agora = new Date();
    const horas = String(agora.getHours()).padStart(2, '0');
    const minutos = String(agora.getMinutes()).padStart(2, '0');
    campoHora.value = `${horas}:${minutos}`;
  }
}

/* Mostra uma ilustração quando o histórico ainda não tem nenhuma ocorrência */
function estadoVazioHistorico() {
  const tabela = document.querySelector('table');
  if (!tabela) return;

  const todasLinhas = tabela.querySelectorAll('tr');
  if (todasLinhas.length > 1) return; // já existe pelo menos 1 ocorrência além do cabeçalho

  const container = document.createElement('div');
  container.style.textAlign = 'center';
  container.style.marginTop = '24px';

  const img = document.createElement('img');
  img.src = '/assets/image/vazio.svg';
  img.alt = 'Nenhuma ocorrência registrada';
  img.style.maxWidth = '180px';
  img.style.opacity = '0.85';

  const texto = document.createElement('p');
  texto.textContent = 'Nenhuma ocorrência registrada ainda.';
  texto.style.color = '#5c6370';

  container.appendChild(img);
  container.appendChild(texto);
  tabela.insertAdjacentElement('afterend', container);
}

/* Copia o texto de cada <th> para um atributo data-label nas células (<td>)
   da mesma coluna, pra usar no layout "cartão" da tabela em telas pequenas
   (o CSS lê esse atributo com content: attr(data-label)). Não precisa
   mexer no HTML: os rótulos são calculados aqui a partir do cabeçalho. */
function aplicarRotulosTabela() {
  const tabela = document.querySelector('table');
  if (!tabela) return;

  const linhas = tabela.querySelectorAll('tr');
  if (linhas.length === 0) return;

  const cabecalho = linhas[0].querySelectorAll('th');
  if (cabecalho.length === 0) return;

  const rotulos = Array.from(cabecalho).map(function (th) {
    return th.textContent.trim();
  });

  for (let i = 1; i < linhas.length; i++) {
    const celulas = linhas[i].querySelectorAll('td');
    celulas.forEach(function (celula, indice) {
      if (rotulos[indice]) {
        celula.setAttribute('data-label', rotulos[indice]);
      }
    });
  }
}
