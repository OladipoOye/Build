import { chakra } from "@chakra-ui/react";

export default function Now() {
    //create animation upon entering page of the pop up for the theme of the month, try to divide it and apply a border radius to get the sam effect
    //the animation should be pop-up like, and ease-in
    //the rest of the page can stay the same
    //rework the modals using state to avoid excess css
    
    return (
        <>
            <head>
                <meta charSet="UTF-8"/>
                <meta name="viewport" content="width=device-width, initial-scale=1" />
                <meta name="description" content="Now in Freedom"/>
                <title>Now in Freedom</title>
            </head>
            <body>
                <div id="Modal_box">
                    <span>&times;</span>
                    <img id="modal_img"/>
                    <div id="caption"></div>
                </div>
                
                <chakra.h2 zIndex='5'  data-state="open"
                  _open={{
                    animationName: "fade-in, scale-in",
                    animationDuration: "1500ms",
                  }}
                  _closed={{
                    animationName: "fade-out, scale-out",
                    animationDuration: "500ms"}} > Theme of <chakra.br/> The <chakra.br/> Month</chakra.h2>

                <div >
                    <img src="../res/ff_2.jpg"/>
                    <div ><h1 >Ch3</h1></div>
                    <div >
                        <img src="#" id="Prov" />
                    </div>
                    <div ><h1 >Ch1</h1></div>
                    <div ><h1 >Ch2</h1></div>
                    <div ><h2>Theme Of The <br/>Month</h2></div>
                </div>
            </body>
        </>
    );
}