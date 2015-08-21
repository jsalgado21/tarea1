define g = Character('goku', color="#000040")
define f = Character('freezer', color="#FF0035")

image goku = "images/goku.jpg"
image freezer = "images/freezer.jpg"
image Namekusei_Destruido = "images/Namekusei_Destruido.jpg"
image Dibujo_Goku = "images/Dibujo_Goku.jpg"



label start:
    
    play sound "music/Enojo_de_Goku.ogg" 
    
    scene Namekusei_Destruido
    show goku at right
    
    g "Hola soy Goku" 
    g "He venido a derrotar a freezer"
    
    
    hide goku
    with dissolve 
    
    show freezer at right
    
    f "Nadie puede derrotarme"
    f " mucho menos un saiyayin como tu"
    
    hide freezer
    with dissolve
    
    show goku_enojado at right
    g " Eso lo veremos"
    g "te mostrare el poder de un supersaiyayin"
    
    hide goku_enojado
    with dissolve
    
    show freezer_2 at right
    f "no digas tonterias"
    
    hide freezer_2
    with dissolve
    
    show goku_supersaiyayin at right
    g" toma esto freezer"
    
    hide goku_supersaiyayin
    with dissolve
    
    show freezer_muriendo at right
    f "no puede seeerr"
    
    stop sound     
    
    
    hide freezer_muriendo
    with dissolve
    
    show Dibujo_Goku at center
    
    ".:. Y asi Goku derroto a Freezer"

    return
    
    
    
    
    
    
    
    
    