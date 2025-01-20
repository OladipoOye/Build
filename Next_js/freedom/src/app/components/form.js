import { revalidatePath } from "next/cache";
import { chakra } from "@chakra-ui/react";

export default async function Prayers() {
    //const response = await fetch("https://6781564085151f714b0a5956.mockapi.io/usr");
    //const usrs = await response.json();
    
    async function addUser(formData) {
        "use server"
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
    
    return(
        <>
            <form action={addUser}>
                <label >Name (optional):</label>
                <input name="name" />
          
                <label >Email (optional):</label>
                <input name="email" />
          
                <label >Prayer</label>
                <textarea name="prayer" required/>
          
                <input type="submit" value="Send" />
            </form>
        </>
    );
}