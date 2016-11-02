(function() {
  $('.navbar-toggle').click(handleIcon);
  var path = window.location.pathname.split('/')[1];
  handleActive(path);

  function handleActive(path){
    $('.'+path).removeClass('nav-bttn');
    $('.'+path).addClass('actv');
  }
  function handleIcon(){
    $('.icon-bar').toggle();
    $('.icon-remove').toggle();
  }
})();
