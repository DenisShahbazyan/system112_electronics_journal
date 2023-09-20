document.addEventListener('DOMContentLoaded', function () {
  var logoutButton = document.getElementById('logoutButton')
  var logoutModal = document.getElementById('logoutModal')
  var confirmLogoutButton = document.getElementById('confirmLogout')
  var cancelLogoutButton = document.getElementById('cancelLogout')
  var exitLogoutButton = document.getElementById('exitLogout')

  var logoutUrl = logoutButton.getAttribute('data-logout-url')

  // При клике на кнопку "Выйти", показываем модальное окно
  logoutButton.addEventListener('click', function () {
    logoutModal.style.display = 'block'
  })

  // При клике на кнопку "Да", разлогиниваем пользователя
  confirmLogoutButton.addEventListener('click', function () {
    window.location.href = logoutUrl // Перенаправляем пользователя на URL-путь для выхода
  })

  // При клике на кнопку "Отмена", скрываем модальное окно
  cancelLogoutButton.addEventListener('click', function () {
    logoutModal.style.display = 'none'
  })
  // При клике на кнопку "X", скрываем модальное окно
  exitLogoutButton.addEventListener('click', function () {
    logoutModal.style.display = 'none'
  })
})
