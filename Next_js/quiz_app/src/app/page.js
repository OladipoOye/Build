"use client"

import { VStack, HStack, Button, AbsoluteCenter, Link, Box} from "@chakra-ui/react";
import { Slide } from '@chakra-ui/transition';
import { useState } from "react";
export default function Home() {
  const [b, setB] = useState(false);
  
  const handleClick = () => {
    setB((prev) => prev? false: true);
  }
  
  return(
    <>
    <AbsoluteCenter>
        <HStack gap="5vw">
            <VStack gap="5vh">
                <Button
                  data-state="open"
                  _open={{
                    animationName: "fade-in, scale-in",
                    animationDuration: "500ms",
                  }}
                  _closed={{
                    animationName: "fade-out, scale-out",
                    animationDuration: "750ms",}}
                  >
                    <Link href="/French" color="black">One</Link>
                </Button>
                <Button
                  data-state="open"
                  _open={{
                    animationName: "fade-in, scale-in",
                    animationDuration: "1000ms",
                  }}
                  _closed={{
                    animationName: "fade-out, scale-out",
                    animationDuration: "500ms"}}
                >
                    <Link href="/Colleges" color="black">One</Link>
                </Button>
            </VStack>
            <VStack gap="5vh">
                <Button
                  data-state="open"
                  _open={{
                    animationName: "fade-in, scale-in",
                    animationDuration: "1250ms",
                  }}
                  _closed={{
                    animationName: "fade-out, scale-out",
                    animationDuration: "500ms"}}
                >
                    One
                </Button>
                <Button
                  data-state="open"
                  _open={{
                    animationName: "fade-in, scale-in",
                    animationDuration: "1500ms",
                  }}
                  _closed={{
                    animationName: "fade-out, scale-out",
                    animationDuration: "500ms"}}
                    onClick={handleClick}
                  >
                    One
                </Button>
            </VStack>
        </HStack>
    </AbsoluteCenter>
    <Slide direction="bottom" in={b} style={{zIndex: 5}} transition="all 750ms ease-out">
        <Box p='40px' color='white' mt='4' bg='red.500'>
          Yes no, i do like to waffle a lot, <br/> However this is the wrong link,<br/> try again.
        </Box>
    </Slide>
    </>
  );
};

