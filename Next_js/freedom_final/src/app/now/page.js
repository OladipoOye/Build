import { chakra } from "@chakra-ui/react";
import { useState } from "react";

const images = [
    "img1", "img2", "img3", "img4"
]

export default function Now() {
    
    //state setting for the modal image src, and the modal image display
    const [imag, setImag ] = useState("#");
    const [disp, setDisp] = useState('none');
    
    //event handlers for setting images as the modal
    const handleClick0 = () => {
        setDisp('block');
        setImag(images[0]);
    }
    
    //event handlers for setting images as the modal
    const handleClick1 = () => {
        setDisp('block');
        setImag(images[1]);
    }
    
    //event handlers for setting images as the modal
    const handleClick2 = () => {
        setDisp('block');
        setImag(images[2]);
    }
    
    //event handlers for setting images as the modal
    const handleClick3 = () => {
        setDisp('block');
        setImag(images[3]);
    }
    
    //event handler for closing the modal image
    const handleClose = () => {
        setDisp('none');
    }
    
    return (
        <>
            <chakra.div id="modalbox" display={disp} zIndex={5} >
                <chakra.span onClick={handleClose} > &times; </chakra.span>
                <chakra.img id="modalimg" src={imag} />
            </chakra.div>
            
            <chakra.div>
                <chakra.img id="mainimg" src="#" />
                
                <chakra.h2 zIndex='5'  data-state="open"
                  _open={{
                    animationName: "fade-in, scale-in",
                    animationDuration: "1500ms",
                  }}
                  _closed={{
                    animationName: "fade-out, scale-out",
                    animationDuration: "500ms"}} > Theme of <br/> The <br/> Month</chakra.h2>
                
                <chakra.h3>Ch1</chakra.h3>
                <chakra.h3>Ch2</chakra.h3>
                <chakra.h3>Ch3</chakra.h3>
                
            </chakra.div>
        </>
    );
}