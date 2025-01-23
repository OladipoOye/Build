"use client"
import { chakra } from "@chakra-ui/react";
import { Box } from "@chakra-ui/react";
import { useState } from "react";

export default function Snippet() {
    const [b, setB] = useState(false);
    
    const handleFocus = () => {
        setB(true);
    }
    
    return (
        <>
            <Box display={ b? 'block' : 'none' } onFocus={handleFocus} transition='500ms ease-in' >
                <chakra.h2> The Freedom Fellowship </chakra.h2>
                <chakra.p>X<br/> Y <br/> Z <br/>, and etc.  </chakra.p>
            </Box>
        </>
    );
} 