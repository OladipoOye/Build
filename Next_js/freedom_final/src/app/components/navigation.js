"use client"
import Link from "next/link";
import { useState } from "react";
import { Stack } from "@chakra-ui/react";
import { HStack } from "@chakra-ui/react";
import { chakra } from "@chakra-ui/react";
import { Slide } from "@chakra-ui/transition";

export default function Navigation() {
    
    //for the menu button toggle
    const [b, setB] = useState(false);
    
    const handleClick = () => {
        setB((prev) => prev? false : true)
    };
    
    return (
        <>
        <Slide direction="left" w="40vw" in={b} style={{zIndex: 5}}>
            <Stack h="100vh" w="40vw" bgColor="blackAlpha.600" gap="10vh">
                <Link href="/about"><chakra.p pt="5vh" pl="30%" textDecor="underline"> About </chakra.p></Link>
                <Link href="/now"><chakra.p pt="5vh" pl="30%" textDecor="underline"> Now </chakra.p></Link>
                <Link href="/contact"><chakra.p pt="5vh" pl="30%" textDecor="underline"> Contact </chakra.p></Link>
                <Link href="/"><chakra.p pt="5vh" pl="30%" textDecor="underline"> Freedom </chakra.p></Link>
            </Stack>
        </Slide>
        
        <HStack>
            <chakra.h2 ml="2vw" minH="5vh" pt="1vh" fontSize="xl">Freedom Fellowship</chakra.h2>
            
            <chakra.button ml="75vw" w="8vw" h="6vh" cursor="pointer" onClick={handleClick} zIndex="8">
                <chakra.div w="3.5vw" h="1.5vh" mb="0.4vh" borderRadius="xl" bgColor={b? "whiteAlpha.600" : "whiteAlpha.950"}></chakra.div>
                <chakra.div w="3.5vw" h="1.5vh" mb="0.4vh" borderRadius="xl" bgColor={b? "whiteAlpha.600" : "whiteAlpha.950"}></chakra.div>
                <chakra.div w="3.5vw" h="1.5vh" borderRadius="xl" bgColor={b? "whiteAlpha.600" : "whiteAlpha.950"}></chakra.div>
            </chakra.button>
        </HStack>
        
        </>
    )
}