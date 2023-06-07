// Объект Quill
var quill = new Quill('#editor', {
  theme: 'snow',
  modules: {
    toolbar: [
    [{ header: [1, 2, 3, false] }],
    ['bold', 'italic', 'underline'],
    [{ 'list': 'ordered' }, { 'list': 'bullet' }],
    ['image', 'link']
    ]
  },
  placeholder: 'Введите текст...'
});

// Подсчет кол-ва слов
var counter = document.getElementById('counter');
quill.on('text-change', function() {
  var text = quill.getText();
  var charCount = text.length;
  counter.textContent = 'Characters: ' + charCount;
});

// Валидация на минимальное кол-во символов
var form = document.querySelector('form');
form.onsubmit = function() {
  var content = document.querySelector('#id_content');
  var minLength = parseInt(content.getAttribute('data-min-length')); // Получение минимальной длины из атрибута

  var editorContent = quill.root.innerHTML.replace(/<p><br><\/p>/g, '<br>');
  var editorText = quill.getText().trim();

  if (editorText.length < minLength) {
    // Если количество символов меньше минимального, предотвратить отправку формы
    alert('Минимальное количество символов: ' + minLength);
    return false;
  }
  content.value = editorContent;
};