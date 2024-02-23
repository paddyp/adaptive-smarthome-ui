import { Component, OnInit, OnDestroy } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { webSocketService } from './services/websocket/websocket.service';
import { HttpClientModule } from '@angular/common/http';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HttpClientModule,],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})


export class AppComponent implements OnInit {
  constructor(private webSocketService: webSocketService) { }
  title = 'user';
  receivedMessages: string[] = [];


  ngOnInit(): void {
    // Connect with websocket
    this.connectWebsocket()
  }

  connectWebsocket(): void {
    this.webSocketService.socket$.subscribe({
      next: (message) => {
        console.log("receive message", message)
      },
      error: (error) => {
        console.error("Websocket error: ", error)
        this.connectWebsocket()
      },
      complete: () => {
        console.log("WebSocket connection closed")
      }
    }
    )
  }


  sendData(): void {
    console.log("send data");
    let out = {
      "method": "get"
    }
    this.webSocketService.send(out);
  }

}
