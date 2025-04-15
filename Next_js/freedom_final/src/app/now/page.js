"use client"
import { chakra } from "@chakra-ui/react";
import { useState } from "react";

const images = [
    "/res/q.png", "/res/Unc.png", "/res/Issac.png"
];

export default function Now() {
    //state setting for the modal image src, and the modal image display
    const [imag, setImag ] = useState("#");
    const [disp, setDisp] = useState('none');
    
    //event handlers for setting images as the modal
    const handleClick0 = () => {
        setDisp('block');
        setImag(images[0]);
        document.querySelector(".bg_img").style.opacity = "0.5";
    }
    
    //event handlers for setting images as the modal
    const handleClick1 = () => {
        setDisp('block');
        setImag(images[1]);
        document.querySelector(".bg_img").style.opacity = "0.5";
    }
    
    //event handlers for setting images as the modal
    const handleClick2 = () => {
        setDisp('block');
        setImag(images[2]);
        document.querySelector(".bg_img").style.opacity = "0.5";

    }
    
    //event handler for closing the modal image
    const handleClose = () => {
        setDisp('none');
        document.querySelector(".bg_img").style.opacity = "1";
    }
    
    return (
        <>
            <chakra.div w="60%" h="60%" id="modalbox" display={disp} pos="absolute" zIndex="12" >
                <chakra.span ml="88vw" onClick={handleClose} cursor="pointer" fontSize="4xl" color="black"> &times; </chakra.span>
                <chakra.img ml="20vw" mt="10vh" id="modalimg" src={imag} />
            </chakra.div>
            
            <chakra.div className="bg_img" h="92vh" w="98vw" pos="relative" transition="0.5s ease">
                <chakra.img mt="0.5vh" ml="1vw" h="100%" w="100%" objectFit="cover" id="mainimg" src="/res/ff_2.jpg"/>
                
                <chakra.h2 pos="absolute" top="40vh" left="42vw" zIndex='5' bgColor="blackAlpha.400" borderRadius="1em" data-state="open"
                  _open={{
                    animationName: "fade-in, scale-in",
                    animationDuration: "3000ms",
                  }}
                  _closed={{
                    animationName: "fade-out, scale-out",
                    animationDuration: "1000ms"}} textDecor="underline" textAlign="center" fontSize="4xl"> Theme of The <br/>Month</chakra.h2>
                
                <chakra.h3 pos="absolute" top="12vh" left="4vw" onClick={handleClick0} zIndex="2" cursor="pointer" color="black">Ch1</chakra.h3>
                <chakra.h3 pos="absolute" top="80vh" left="4vw" onClick={handleClick1} zIndex="2" cursor="pointer" color="black">Ch2</chakra.h3>
                <chakra.h3 pos="absolute" top="80vh" left="88vw" onClick={handleClick2} zIndex="2" cursor="pointer" color="black">Ch3</chakra.h3>
                
            </chakra.div>
        </>
    );
}