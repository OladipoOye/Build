"use client"
import { chakra } from "@chakra-ui/react";
import { Box } from "@chakra-ui/react";

export default function Snippet() {
    //snippet section, in the form of a box, with a title and body (animations included)
    return (
            <Box color="black" w="100%" h="50vh" bg="white">
                <chakra.h1 fontSize="2xl" textDecoration="underline" data-state="open"
                  _open={{
                    animationName: "slide-from-right-full, scale-in",
                    animationDuration: "750ms",
                  }}
                  _closed={{
                    animationName: "fade-out, scale-out",
                    animationDuration: "1000ms",}} textAlign="center" > 
                    The Freedom Fellowship 
                </chakra.h1>
                
                <chakra.p data-state="open"
                  _open={{
                    animationName: "fade-in, scale-in",
                    animationDuration: "2000ms",
                  }}
                  _closed={{
                    animationName: "fade-out, scale-out",
                    animationDuration: "1000ms",}} >
                    X<br/>Y <br/> Z <br/>, and etc.  
                </chakra.p>
            </Box>
    );
} 