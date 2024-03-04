import { Component, OnInit, NgModule } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { webSocketService } from './services/websocket/websocket.service';
import { HttpClientModule } from '@angular/common/http';
import { SmartHomeViewComponent } from './tabs/smart-home-view/smart-home-view.component';
import { AdaptUIViewComponent } from './tabs/adapt-uiview/adapt-uiview.component';
import { ContextOfUseViewComponent } from './tabs/context-of-use-view/context-of-use-view.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    HttpClientModule,
    CommonModule,
    SmartHomeViewComponent,
    AdaptUIViewComponent,
    ContextOfUseViewComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})


export class AppComponent implements OnInit {
  constructor(private webSocketService: webSocketService) { }
  title = 'admin';
  receivedMessages: string[] = [];
  retries = 0
  schema: any
  currentTab: string = "contextofuse";
  private _possibleCurrentTab = ['contextofuse', 'smarthomedevices', 'adaptuirules']

  ngOnInit(): void {
    // Connect with websocket
    this.connectWebsocket()
  }

  connectWebsocket(): void {
    this.webSocketService.socket$.subscribe({
      next: (message) => {
        console.log("receive message", message)
        if (message.schema) {
          console.log("test")
          this.schema = message.schema
        } else {
          console.log(typeof (message))
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

  changeView(view: string): void {
    if (this._possibleCurrentTab.includes(view)) {
      this.currentTab = view;
    }
  }
  sendData(): void {
    // console.log("send data");
    // let test = {
    //   'method': 'create',
    //   'group': 'smarthomedevice',
    //   'payload': {
    //     "name": "Test",
    //     "icon": "LAMP",
    //     "channels":
    //       [
    //         { "channel_no": 1, "type": "INT" }
    //       ]
    //   }
    // }
    let test = {
      'method': 'get',
      'type': 'schema',
      'schema': 'smarthome'
    }
    this.webSocketService.send(test);
  }

}
