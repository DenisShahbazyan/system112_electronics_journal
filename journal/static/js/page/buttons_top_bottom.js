$(function () {
  $(window).scroll(function () {
    if ($(window).scrollTop() > 100) {
      $('#scroll_top').show()
    } else {
      $('#scroll_top').hide()
    }
  })

  $('#scroll_top').click(function () {
    $('html, body').animate({ scrollTop: 0 }, 100)
    return false
  })
})

$(function () {
  $(window).scroll(function () {
    if ($(window).scrollTop() + $(window).height() >= $(document).height()) {
      $('#scroll_bottom').hide()
    } else {
      $('#scroll_bottom').show()
    }
  })

  $('#scroll_bottom').click(function () {
    $('html, body').animate(
      { scrollTop: $(document).height() - $(window).height() },
      100
    )
    return false
  })
})

$(function () {
  if ($(document).height() <= $(window).height()) {
    $('#scroll_bottom').hide()
  }
})
