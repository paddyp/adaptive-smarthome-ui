import { Component, OnInit, OnDestroy } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { webSocketService } from './services/websocket/websocket.service';
import { HttpClientModule } from '@angular/common/http';
import { webSocket } from 'rxjs/webSocket';


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
    this.webSocketService.socket$.subscribe(
      (message) => {
        console.log("receive message", message)
      },
      (error) => {
        console.error("Websocket error: ", error)
      },
      () => {
        console.log("WebSocket connection closed")
      }
    )

  }


  sendData(): void {
    console.log("send data");
    this.webSocketService.send("hallo");
  }

}
