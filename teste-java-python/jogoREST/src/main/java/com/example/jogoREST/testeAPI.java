package com.example.jogoREST;


import org.springframework.web.bind.annotation.*;
import org.springframework.stereotype.Controller;
import org.springframework.beans.factory.annotation.Autowired;

@RestController
@RequestMapping("/demo")
public class testeAPI {
    @Autowired
    private TesteRepositorio testeRepositorio;

    @GetMapping("/add/{name}")
    public String endPoint(@PathVariable String name){
        TesteModel n = new TesteModel();
        String nomeFormatado = name.substring(2, name.length()-3);
        if(nomeFormatado.isEmpty()){
            return "Bad Request";
        }

        n.setName(nomeFormatado);
        testeRepositorio.save(n);
        return "Saved";
    }

    @GetMapping(path="/all")
    public @ResponseBody Iterable<TesteModel> getAllUsers() {
        // This returns a JSON or XML with the users
        return testeRepositorio.findAll();
    }
}
