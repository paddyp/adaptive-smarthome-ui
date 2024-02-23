import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';


@Injectable({
  providedIn: 'root',
})
export class webSocketService {
  public socket$!: WebSocketSubject<any>;

  constructor() {
    this.connect()
  }

  connect() {
    this.socket$ = webSocket("ws://localhost:8000/ws");
  }

  disconnect() {
    this.socket$.complete();
  }

  isConnected(): boolean {
    return (this.socket$ === null ? false : !this.socket$.closed)
  }

  onMessage(): Observable<any> {
    return this.socket$.asObservable().pipe(
      map(message => message)
    );
  }

  send(message: any) {
    this.socket$.next(message);
  }

}