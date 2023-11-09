import { Injectable } from '@angular/core';
import {HttpClient, HttpErrorResponse} from "@angular/common/http";
import {catchError, Observable, tap, throwError} from "rxjs";
import {Pokemon} from "../models/pokemon";

@Injectable({
  providedIn: 'root'
})
export class PokemonService {

  private pokemonsUrl: string = "http://localhost:8000/api/pokemons";

  constructor(private http: HttpClient) { }

  getPokemons(): Observable<Pokemon[]> {
    return this.http.get<Pokemon[]>(this.pokemonsUrl).pipe(
      tap(data => console.log('All', JSON.stringify(data))),
      catchError(this.handleError)
    )
  }
  private handleError(err: HttpErrorResponse): Observable<never>{
    let errorMessage: string = "";
    if (err.error instanceof ErrorEvent){
      errorMessage = `Server return code ${err.status}, error message is: ${err.message}`;
    }
    console.error(errorMessage)
    return throwError(() => errorMessage);
  }
}
