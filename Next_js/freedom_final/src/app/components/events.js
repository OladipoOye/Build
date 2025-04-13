"use client"
import { Box, HStack } from "@chakra-ui/react";
import { chakra } from "@chakra-ui/react";

export default function Events() {
    //event boxes, lined horizontally with images and the descriptions
    return (
            <Box bg="white" w="100%" h="60vh">
                    <chakra.h2 textAlign='center' color="black" textDecoration='underline' fontSize='2xl' > Events </chakra.h2>
                    <HStack ml="2vw" mt="4vh" gap="2vw" w='100%' >
                        
                        <Box w="30%" border=" 2px dashed black" borderRadius="2em" bg="black" h='50vh' >  
                            <chakra.h3 textDecoration="underline" textAlign='center' color='white' fontWeight='bold' > Event x</chakra.h3> 
                            <chakra.img src='#' h="20%" w="80%" alt='event x' />
                            <chakra.p color='white'> Event x is the x event of the year<chakra.br/> covering y and z </chakra.p> 
                        </Box>
                        <Box w="30%" border=" 2px dashed black" borderRadius="2em" bg="black" h='50vh' > 
                            <chakra.h3 textDecoration="underline" textAlign='center' color='white' fontWeight='bold' > Event y</chakra.h3>
                            <chakra.img src='#' h="20%" w="80%" alt='event y' /> 
                            <chakra.p>Event y is the y event of the year<chakra.br/> covering something and something else </chakra.p> 
                        </Box>
                        <Box w="30%" border=" 2px dashed black" borderRadius="2em" bg="black" h='50vh' >
                            <chakra.h3 textDecoration="underline" textAlign='center' color='white' fontWeight='bold' > Event z</chakra.h3> 
                            <chakra.img src='#' h="20%" w="80%" alt='event z' />
                            <chakra.p> Event z is the z event of the year<chakra.br/> allowing for x and z to happen also </chakra.p> 
                        </Box>
                    
                    </HStack>
            </Box>
            );
}