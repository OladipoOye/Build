import { AspectRatio, Box, HStack} from '@chakra-ui/react';
import { chakra } from '@chakra-ui/react';

export default function Events() {
    return (
        <>
            <Box>
                <chakra.h2 textAlign='center' textDecoration='underline' fontSize='2xl' > Events </chakra.h2>
                <HStack gap="2vw" w='100%' >
                    
                    <Box w="20%" border=" 2px dashed black" borderRadius="2em" bg="black" h='80vh' > 
                        <AspectRatio ratio={1}> <chakra.img src='#' alt='event x' /> </AspectRatio> 
                        <chakra.h3 textAlign='center' color='white' fontWeight='bold' > Event x</chakra.h3> 
                        <chakra.p color='white'> Event x is the x event of the year<chakra.br/> covering y and z </chakra.p> 
                    </Box>
                    <Box w="20%" border=" 2px dashed black" borderRadius="2em" bg="black" h='80vh' > 
                        <AspectRatio ratio={1}> <chakra.img src='#' alt='event y' /> </AspectRatio> 
                        <chakra.h3 textAlign='center' color='white' fontWeight='bold' > Event y</chakra.h3> 
                        <chakra.p>Event y is the y event of the year<chakra.br/> covering something and something else </chakra.p> 
                    </Box>
                    <Box w="20%" border=" 2px dashed black" borderRadius="2em" bg="black" h='80vh' > 
                        <AspectRatio ratio={1}> <chakra.img src='#' alt='event z' /> </AspectRatio> 
                        <chakra.h3 textAlign='center' color='white' fontWeight='bold' > Event z</chakra.h3> 
                        <chakra.p> Event z is the z event of the year<chakra.br/> allowing for x and z to happen also </chakra.p> 
                    </Box>
                   
                </HStack>
            </Box>
        </>
    );
};