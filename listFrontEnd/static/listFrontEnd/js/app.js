window.onload=()=>{
    let passView = document.getElementById('viewPass');
    passView.addEventListener('click',()=>{
        let passInput = document.getElementById('pass');;
        if ( passInput.getAttribute('type') == 'password' ){
            passInput .setAttribute('type','text');
            passView.setAttribute('src','{% static "listFrontEnd/images/icons8-eye-40.png" %}') 
        }else{
            passInput .setAttribute('type','password');
            passView.setAttribute('src','{% static "listFrontEnd/images/icons8-invisible-40.png" %}')
        }
    })
}
        
        