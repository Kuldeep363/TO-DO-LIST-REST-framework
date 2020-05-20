window.onload=()=>{
    let check = document.getElementById('check')
    check.addEventListener('click',()=>{
        setTimeout(()=>{
            const title = document.getElementById('task').value;
            const date = document.getElementById('date').value;
            flag = 1
            // console.log(title,date)
            if(title == '' || title == null){
                task_err = document.getElementById('task_error')
                task_err.innerHTML = 'Please Add Task'
                task_err.style.color = 'red'
                flag = 0
            }
            else{
                task_err = document.getElementById('task_error')
                task_err.innerHTML = ''
            }
            if(date == '' || date == null){
                date_err = document.getElementById('date_error')
                date_err.innerHTML = 'Please Enter Deadline For Task'
                date_err.style.color = 'red'
                flag = 0
            }
            else{
                date_err = document.getElementById('date_error')
                date_err.innerHTML = ''
            }
    
            if(flag == 1){
                document.getElementById('submit').click()
            }
        },2000)
        
    })
    

    let h = document.querySelectorAll('.title');
    let tasks = document.getElementsByClassName('task-status');
    console.log(h,h.length)
    console.log(tasks)
    for(let i=0;i<h.length;i++){
        console.log(i)
        for(let j=i;j<i+2;j++){
            tasks[j+i].style.lineHeight = h[i].clientHeight + 'px';
            console.log(h[i])
        }               
    }

    // let show = document.querySelectorAll('.more.btn')
    // let hide = document.querySelectorAll('.less.btn')
    // let task = document.querySelectorAll('.task-description')
    // let task1 = document.querySelectorAll('.task-description')
    // for(let i=0;i<show.length;i++){
    //     show[i].addEventListener('click',()=>{
    //     task[i].classList.toggle('display');
    //     show[i].style.display = 'none'
    //     })
    //     hide[i].addEventListener('click',()=>{
    //     task1[i].classList.toggle('display');
    //     show[i].style.display = 'inline-block'
    //     })
    // }
                
}
