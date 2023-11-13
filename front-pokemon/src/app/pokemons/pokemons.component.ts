import {Component, OnDestroy, OnInit} from '@angular/core';
import {last, Subscription} from "rxjs";
import {PokemonService} from "../pokemon/pokemon.service";
import {Pokemon} from "../models/pokemon";
import {Type} from "../models/type";

@Component({
  selector: 'app-pokemons',
  templateUrl: './pokemons.component.html',
  styleUrls: ['./pokemons.component.scss']
})
export class PokemonsComponent implements OnInit, OnDestroy{

  errorMessage: string = '';
  sub!: Subscription;

  pokemons: Pokemon[] = [];

  pokemon!: Pokemon;

  constructor(private pokemonService: PokemonService) { }

  ngOnDestroy(): void {
    this.sub.unsubscribe();
  }

  ngOnInit(): void {
    this.sub = this.pokemonService.getPokemons().subscribe({
      next: pokemons => {
        this.pokemons = pokemons;
      },
      error: err => this.errorMessage = err
    });
  }

  setPokemon(pokemon: Pokemon): void{
    this.pokemon = pokemon;
  }
}
