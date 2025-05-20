window.onscroll = function() {
    if(window.innerHeight + window.scrollY >= document.body.offsetHeight)
    {
        document.querySelector('body').style.backgroundColor = 'green';

    }else{
        document.querySelector('body').style.backgroundColor = 'white';
    }
};