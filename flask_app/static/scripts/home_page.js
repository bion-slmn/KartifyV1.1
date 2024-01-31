
$(document).ready(function () {
  $('#all').click(function () {
    $('html').animate({
      scrollTop: $('#startShopping').offset().top
    }, 1500);
  });

  $('.card').click(function () {
    const id = $(this).attr('id')
    window.open(`search?searchName=${id}`, '_self');
  });
});
