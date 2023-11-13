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
  filteredPokemons: Pokemon[] = [];

  pokemon!: Pokemon;

  constructor(private pokemonService: PokemonService) { }

  ngOnDestroy(): void {
    this.sub.unsubscribe();
  }

  ngOnInit(): void {
    this.sub = this.pokemonService.getPokemons().subscribe({
      next: pokemons => {
        this.pokemons = pokemons;
        this.filteredPokemons = pokemons;
      },
      error: err => this.errorMessage = err
    });
    this.filteredPokemons = this.pokemons;
  }

  setPokemon(pokemon: Pokemon): void{
    this.pokemon = pokemon;
  }
}
