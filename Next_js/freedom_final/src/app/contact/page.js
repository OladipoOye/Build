"use client"
import { Box } from "@chakra-ui/react";
import { AspectRatio } from "@chakra-ui/react";
import Prayers from "../components/form";
import { chakra } from "@chakra-ui/react";

export default function Contact() {
    return (
        <>
            <Box display="absolute" w="100vw" h="100vh" bgColor="blackAlpha.950">
                
                {/* <chakra.div id="topleft" > 
                    <Prayers />
                </chakra.div> */}
                
                <chakra.div id="topright" pos="absolute" top="10vh" right="2vw" maxH="60vh" maxW="60vw" >
                    <chakra.iframe src="https://www.youtube.com/@wearefreedomk/" allowFullScreen></chakra.iframe>
                </chakra.div>
                
                <chakra.div id="bottomleft" pos="absolute" left="2vw" bottom="10vh" maxW="40vw" >
                    <chakra.p>
                    Service times: Every other wednesday, 7pm<br/>
                    Location: Snoddhurst Bottom, Chatham ME5 OLU<br/>
                    Contact no:
                    </chakra.p>
                </chakra.div>
                
                <chakra.div id="bottomright" pos="absolute" right="20vw" bottom="10vh" h="50vh" w="20vw">
                    <chakra.iframe borderRadius="1em" h="50vh" w="40vw" src="https://www.instagram.com/wearefreedomkent/embed/" allowFullScreen></chakra.iframe>
                </chakra.div>
                
            </Box>
        </>
    );
}