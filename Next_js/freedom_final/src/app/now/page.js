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
                <chakra.span ml="88vw" onClick={handleClose} cursor="pointer" fontSize="4xl" color="white"> &times; </chakra.span>
                <chakra.img ml="20vw" mt="10vh" id="modalimg" src={imag} />
            </chakra.div>
            
            <chakra.div className="bg_img" pos="relative" transition="0.5s ease">
                <chakra.img opacity="0.7" mt={["8vh", "0.5vh"]} ml={["0", "5vw"]}  h={["60vh", "88vh"]} w={["100vw", "90vw"]} objectFit={["contain", "cover"]} id="mainimg" src="/res/ff_2.jpg"/>
                
                {/* theme of the month popup */}
                <chakra.h2
                    pos="absolute"
                    top={["30vh", "40vh"]} 
                    left={["30vw", "42vw"]} 
                    zIndex="5"
                    bgColor="blackAlpha.400"
                    borderRadius="1em"
                    data-state="open"
                    _open={{
                        animationName: "fade-in, scale-in",
                        animationDuration: "3000ms",
                    }}
                    _closed={{
                        animationName: "fade-out, scale-out",
                        animationDuration: "1000ms",
                    }}
                    textDecor="underline"
                    textAlign="center"
                    fontSize={["2xl", "4xl"]} >
                    Theme of The <br /> Month
                </chakra.h2>
                    
                    {/* the chapters for the month */}
                <chakra.h3
                    pos="absolute"
                    top={["8vh", "12vh"]} 
                    left={["5vw", "8vw"]} 
                    onClick={handleClick0}
                    zIndex="2"
                    cursor="pointer"
                    fontWeight="bold"
                    fontSize={["lg", "xl"]} 
                    color={["white", "black"]}>
                    Ch1
                </chakra.h3>
                <chakra.h3
                    pos="absolute"
                    top={["70vh", "80vh"]} 
                    left={["5vw", "8vw"]} 
                    onClick={handleClick1}
                    zIndex="2"
                    cursor="pointer"
                    fontWeight="bold"
                    fontSize={["lg", "xl"]} 
                    color={["white", "black"]}>
                    Ch2
                </chakra.h3>
                <chakra.h3
                    pos="absolute"
                    top={["70vh", "80vh"]} 
                    right={["5vw", "12vw"]} 
                    onClick={handleClick2}
                    zIndex="2"
                    cursor="pointer"
                    fontWeight="bold"
                    fontSize={["lg", "xl"]} 
                    color={["white", "black"]}>
                    Ch3
                </chakra.h3>
        </chakra.div>
    </>);
}