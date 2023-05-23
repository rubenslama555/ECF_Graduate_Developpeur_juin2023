const form=document.querySelector('form');
const submit=document.querySelector('submit');
submit.addEventListener('click'),(event) =>{
    event.preventDefault();
}
    const formData=new FormData(form);
    fetch('reservation.html',{
        method:'POST',body:formData
})
.then(response =>{
    console.log('Les donnees ont ete envoyee avec succees');

form.reset();
})
.catch(err=>{console.error('une erreur est survenue, veuillez reesayer plus tard');
})
window.location.href = "Signup.html";