import { Component, OnInit, OnDestroy, ChangeDetectionStrategy, ChangeDetectorRef } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { webSocketService } from './services/websocket/websocket.service';
import { HttpClientModule } from '@angular/common/http';
import { SmTableComponent } from './sm-table/sm-table.component';
import { FormsModule } from '@angular/forms';
import { SmDeviceIconComponent } from './sm-device-icon/sm-device-icon.component';

import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HttpClientModule, SmTableComponent, FormsModule, CommonModule, SmDeviceIconComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
  changeDetection: ChangeDetectionStrategy.Default
})


export class AppComponent implements OnInit {
  constructor(private webSocketService: webSocketService, private cdr: ChangeDetectorRef) { }
  title = 'smarthome';
  data: any[] = [];

  ngOnInit(): void {
    // Connect with websocket
    this.connectWebsocket()
    this.getData()
  }

  connectWebsocket(): void {
    this.webSocketService.socket$.subscribe({
      next: (message) => {
        console.log("receive message")
        console.log(typeof (message))
        console.log(message)

        if (message.method && message.method == "broadcast" && message.type && message.type == "data" && message.data) {
          this.data = message.data.smarthomeview
          console.log(this.data)
          this.cdr.detectChanges();
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


  getData(): void {
    let payload = {
      'method': 'get',
      'type': 'data'

    }
    this.webSocketService.send(payload);
  }

}
