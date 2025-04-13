"use client"
import { Box, HStack } from "@chakra-ui/react";
import { chakra } from "@chakra-ui/react";
import { useEffect } from "react";

function hov() {
    //hover function for the event boxes
    const box = document.querySelectorAll(".box");
    box.forEach((b) => {
        b.addEventListener("mouseover", () => {
            b.style.backgroundColor = "white";
            b.style.zIndex = "10";
            b.style.transition = "0.5s";
            b.style.transform = "scale(1.4)";
            b.style.color = "black";
        });
        b.addEventListener("mouseout", () => {
            b.style.backgroundColor = "black";
            b.style.zIndex = "1";
            b.style.transition = "0.5s";
            b.style.transform = "scale(1)";
            b.style.color = "white";
        });
    });
}

export default function Events() {
    useEffect(() => {
        hov(); // Call the hover function after the component mounts
    }, []);
    //event boxes, lined horizontally with images and the descriptions
    return (
            <Box bg="white" w="100%" h="80vh">
                    <chakra.h2 textAlign='center' color="black" textDecoration='underline' fontSize='2xl' > Events </chakra.h2>
                    <HStack ml="2vw" mt="4vh" gap="2vw" w='100%' >
                        
                        <Box className="box" color="white" w="30%" borderRadius="2em" bg="black" h='50vh'>  
                            <chakra.h3 textDecoration="underline" textAlign='center' fontWeight='bold' > Event x</chakra.h3> 
                            <chakra.img src='#' h="20%" w="80%" alt='event x' />
                            <chakra.p p="8%"> Event x is the x event of the year<chakra.br/> covering y and z </chakra.p> 
                        </Box>
                        <Box className="box" color="white" w="30%" borderRadius="2em" bg="black" h='50vh' > 
                            <chakra.h3 textDecoration="underline" textAlign='center' fontWeight='bold' > Event y</chakra.h3>
                            <chakra.img src='#' h="20%" w="80%" alt='event y' /> 
                            <chakra.p p="8%">Event y is the y event of the year<chakra.br/> covering something and something else </chakra.p> 
                        </Box>
                        <Box className="box" color="white" w="30%" borderRadius="2em" bg="black" h='50vh' >
                            <chakra.h3 textDecoration="underline" textAlign='center' fontWeight='bold' > Event z</chakra.h3> 
                            <chakra.img src='#' h="20%" w="80%" alt='event z' />
                            <chakra.p p="8%"> Event z is the z event of the year<chakra.br/> allowing for x and z to happen also </chakra.p> 
                        </Box>
                    
                    </HStack>
            </Box>
            );
}