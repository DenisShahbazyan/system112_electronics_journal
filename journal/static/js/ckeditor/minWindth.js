document.addEventListener('DOMContentLoaded', function () {
  var ckEditors = document.querySelectorAll('.ck-editor')

  ckEditors.forEach(function (editor) {
    editor.style.minWidth = '100%'
  })
})
