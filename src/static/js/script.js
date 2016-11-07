(function() {
  $('.navbar-toggle').click(handleIcon);
  var path = window.location.pathname.split('/')[1];
  var form_check = formInit();
  handleActive(path);
  //form init
  formCheck();
  addFormCheck('email',0);
  addFormCheck('username',1);
  addFormCheck('github_handle',2);
  addFormCheck('password1',3);
  addFormCheck('password2',4);

  // Adding grid to form
  $('#id_first_name').parent().addClass('col-md-6');
  $('#id_last_name').parent().addClass('col-md-6');
  $('#id_email').parent().addClass('col-md-12');
  $('#id_username').parent().addClass('col-md-6');
  $('#id_github_handle').parent().addClass('col-md-6');
  $('#id_phone').parent().addClass('col-md-12');
  $('#id_age').parent().addClass('col-md-6');
  $('#id_gender').parent().addClass('col-md-6');
  $('#id_password1').parent().addClass('col-md-12');
  $('#id_password2').parent().addClass('col-md-12');

  $('#id_gender').prev().addClass('active highlight');
  //Removing `req` class from not required fields
  $('#id_first_name').prev().find('.req').hide();
  $('#id_last_name').prev().find('.req').hide();
  $('#id_phone').prev().find('.req').hide();
  $('#id_age').prev().find('.req').hide();

  //end form init

  $('form').find('input, textarea').on('keyup blur focus', function (e) {

  var $this = $(this),
      label = $this.prev('label');

	  if (e.type === 'keyup') {
			if ($this.val() === '') {
          label.removeClass('active highlight');
        } else {
          label.addClass('active highlight');
        }
    } else if (e.type === 'blur') {
    	if( $this.val() === '' ) {
    		label.removeClass('active highlight');
			} else {
		    label.removeClass('highlight');
			}
    } else if (e.type === 'focus') {

      if( $this.val() === '' ) {
    		label.removeClass('highlight');
			}
      else if( $this.val() !== '' ) {
		    label.addClass('highlight');
			}
    }

  });

  function formInit(){
    var form_check=[false,false,false,false,false];
    var fName = $('#id_first_name').val();
    var lName = $('#id_last_name').val();
    var email = $('#id_email').val();
    var username = $('#id_username').val();
    var github_handle = $('#id_github_handle').val();
    var phone = $('#id_phone').val();
    var age = $('#id_age').val();
    if(fName!=null && fName != ""){
      $('#id_first_name').prev().addClass('active highlight');
    }
    if(lName!=null && lName != ""){
      $('#id_last_name').prev().addClass('active highlight');
    }
    if(email==null || email == ""){
      form_check[0]=false;
    }else{
      form_check[0]=true;
      $('#id_email').prev().addClass('active highlight');
    }
    if(username==null || username == ""){
      form_check[1]=false;
    }else{
      form_check[1]=true;
      $('#id_username').prev().addClass('active highlight');
    }
    if(github_handle==null || github_handle == ""){
      form_check[2]=false;
    }else{
      form_check[2]=true;
      $('#id_github_handle').prev().addClass('active highlight');
    }
    if(phone!=null && phone != ""){
      $('#id_phone').prev().addClass('active highlight');
    }
    if(age!=null && age != ""){
      $('#id_age').prev().addClass('active highlight');
    }
    return form_check;
  }
  function addFormCheck(id, number){
    $(document.body).on('input keyup', '#id_'+id,
        function() {
          var input = $(this).val();
          if(input==null || input == ""){
            form_check[number]=false;
          }else{
            form_check[number]=true;
          }
          formCheck();
    });
  }
  function formCheck(){
    if(form_check[0] === true && form_check[1] === true && form_check[2] && form_check[3] && form_check[4]){
      $('#submit').removeAttr('disabled',null);
    }else{
      $('#submit').attr('disabled',true);
    }
  }
  function handleActive(path){
    $('.'+path).removeClass('nav-bttn');
    $('.'+path).addClass('actv');
  }
  function handleIcon(){
    $('.icon-bar').toggle();
    $('.icon-remove').toggle();
  }
})();
