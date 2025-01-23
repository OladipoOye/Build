"use client"
import { chakra } from "@chakra-ui/react";
import { Box } from "@chakra-ui/react";

export default function Snippet() {
    //snippet section, in the form of a box, with a title and body (animations included)
    return (
            <Box>
                <chakra.h2 data-state="open"
                  _open={{
                    animationName: "slide-from-right-full, scale-in",
                    animationDuration: "500ms",
                  }}
                  _closed={{
                    animationName: "fade-out, scale-out",
                    animationDuration: "750ms",}} textAlign="center" > 
                    The Freedom Fellowship 
                </chakra.h2>
                
                <chakra.p data-state="open"
                  _open={{
                    animationName: "fade-in, scale-in",
                    animationDuration: "1500ms",
                  }}
                  _closed={{
                    animationName: "fade-out, scale-out",
                    animationDuration: "750ms",}} >
                    X<br/>Y <br/> Z <br/>, and etc.  
                </chakra.p>
            </Box>
    );
} 