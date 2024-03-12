import { Component, OnInit, OnDestroy } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { webSocketService } from './services/websocket/websocket.service';
import { HttpClientModule } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { UIElement, ElementsEnum, TypeEnum } from './interfaces/uielement';
import { ButtonComponent } from './uielements/button/button.component';
import { RangeComponent } from './uielements/range/range.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HttpClientModule, CommonModule, ButtonComponent, RangeComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})


export class AppComponent implements OnInit {
  constructor(private webSocketService: webSocketService) { }
  title = 'user';
  receivedMessages: string[] = [];
  elements: Array<UIElement> = [
    {
      "id": 1,
      "uielement": ElementsEnum.BUTTON,
      "name": "Set Temperatur to 20",
      "current_value": 1,
      "min": 0,
      "max": 20,
      "step": 1,
      "min_color": "#777777",
      "max_color": "#FFFFFF",
      "values": [
        {
          "id": 1,
          "name": "Temperature",
          "contextofuse": {
            "id": 1,
            "key": "key",
            "value": "value",
            "type": TypeEnum.INT
          },
        }
      ],
      "description": "This is a description",
      "orderlevel": 2
    },
    {
      "id": 2,
      "uielement": ElementsEnum.SLIDER,
      "name": "Set Temperatur to 20",
      "current_value": 1,
      "min": 0,
      "max": 20,
      "step": 1,
      "min_color": "#777777",
      "max_color": "#FFFFFF",
      "values": [
        {
          "id": 1,
          "name": "Temperature",
          "contextofuse": {
            "id": 1,
            "key": "key",
            "value": "value",
            "type": TypeEnum.INT
          },
        }
      ],
      "description": "This is a description",
      "orderlevel": 1
    }
  ];

  ngOnInit(): void {
    // Connect with websocket
    this.connectWebsocket()
    this.getData();
  }

  connectWebsocket(): void {
    this.webSocketService.socket$.subscribe({
      next: (message) => {
        console.log("receive message", message)
        if (message.method && message.method == "broadcast" && message.type && message.type == "data" && message.data) {
          this.elements = message.data.userview

        }
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

  updateEvent(event: any): void {
    console.log("send", event);
    this.webSocketService.send(event);
  }

  getData(): void {
    let payload = {
      'method': 'get',
      'type': 'data'

    }
    this.webSocketService.send(payload);
  }

}
