"use client"
import { Box } from "@chakra-ui/react";
import { AspectRatio } from "@chakra-ui/react";
import Prayers from "../components/form";
import { chakra } from "@chakra-ui/react";

export default function Contact() {
    return (
        <>
            <Box display="absolute">
                
                {/* <chakra.div id="topleft" > 
                    <Prayers />
                </chakra.div> */}
                
                <chakra.div id="topright" marginRight="2vw" marginTop="2vh" maxH="60vh" maxW="60vw" >
                    <chakra.iframe src="https://www.youtube.com/@wearefreedomk/" allowFullScreen></chakra.iframe>
                </chakra.div>
                
                <chakra.div id="bottomleft" marginLeft="2vw" marginBottom="2vh" >
                    <chakra.p>
                    Service times: Every other wednesday, 7pm<br/>
                    Location: Snoddhurst Bottom, Chatham ME5 OLU<br/>
                    Contact no:
                    </chakra.p>
                </chakra.div>
                
                <chakra.div id="bottomright" marginRight="2vw" marginTop="2vh" maxH="60vh" maxW="60vw" >
                    <chakra.iframe src="https://www.instagram.com/wearefreedomkent/embed/" allowFullScreen></chakra.iframe>
                </chakra.div>
                
            </Box>
        </>
    );
}