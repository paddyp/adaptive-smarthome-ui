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
  title = 'admin';
  receivedMessages: string[] = [];
  retries = 0

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
    let test = {
      'method': 'create',
      'group': 'smarthomedevice',
      'payload': {
        "name": "Test",
        "icon": "LAMP",
        "channels":
          [
            { "channel_no": 1, "type": "INT" }
          ]
      }
    }
    // let test = {
    //   'method': 'get',
    //   'type': 'data',
    // }
    this.webSocketService.send(test);
  }

}
