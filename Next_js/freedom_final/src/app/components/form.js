"use server"
import { revalidatePath } from "next/cache";
import { chakra } from "@chakra-ui/react";


export default async function Prayers() {
    async function addUser(formData) {
        const name = formData.get("name")
        const res = await fetch("https://6781564085151f714b0a5956.mockapi.io/usr",
            {
                method: "POST",
                headers: {
                    "Content-Type":"application/json"
                }, 
                body: JSON.stringify({ name }), }
            );
        const newUser = await res.json();
        revalidatePath("/mock-users");
        //console.log(newUser)
    };
    
    return (
        <>
            <chakra.h4>Leave a prayer:</chakra.h4>
            <chakra.form action={addUser}>
                <chakra.label >Name (optional):</chakra.label>
                <chakra.input name="name" />
          
                <chakra.label >Email (optional):</chakra.label>
                <chakra.input name="email" />
          
                <chakra.label >Prayer</chakra.label>
                <chakra.textarea name="prayer" required/>
          
                <chakra.input type="submit" value="Send" />
            </chakra.form>
        </>
    );
}