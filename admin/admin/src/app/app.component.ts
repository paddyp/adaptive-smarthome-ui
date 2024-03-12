import { Component, OnInit, NgModule } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { webSocketService } from './services/websocket/websocket.service';
import { HttpClientModule } from '@angular/common/http';
import { SmartHomeViewComponent } from './tabs/smart-home-view/smart-home-view.component';
import { AdaptUIViewComponent } from './tabs/adapt-uiview/adapt-uiview.component';
import { ContextOfUseViewComponent } from './tabs/context-of-use-view/context-of-use-view.component';
import { CommonModule } from '@angular/common';
import { ChangeDetectorRef } from '@angular/core';
import { UielementComponent } from './tabs/uielement/uielement.component';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    HttpClientModule,
    CommonModule,
    SmartHomeViewComponent,
    AdaptUIViewComponent,
    ContextOfUseViewComponent,
    UielementComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss',
})


export class AppComponent implements OnInit {
  constructor(private webSocketService: webSocketService, private changeDetectorRef: ChangeDetectorRef) { }
  title = 'admin';
  receivedMessages: string[] = [];
  retries = 0
  schema: any
  smartHomeDeviceSchema: object = {};
  contextOfUseSchema: object = {};
  adaptUIRUleSchema: object = {};
  uielementSchema: object = {};


  currentTab: string = "";
  data: object = {};
  private _possibleCurrentTab = ['contextofuse', 'smarthomedevices', 'adaptuirules', 'uielement']

  ngOnInit(): void {
    // Connect with websocket
    this.connectWebsocket()
    this.getData();
    this.getSchemas();
  }

  connectWebsocket(): void {
    this.webSocketService.socket$.subscribe({
      next: (message) => {
        console.log("receive message", message)
        if (message.schemas) {
          this.smartHomeDeviceSchema = message.schemas.smarthome
          this.contextOfUseSchema = message.schemas.contextofuse;
          this.adaptUIRUleSchema = message.schemas.adaptrules;
          this.uielementSchema = message.schemas.uielement;
        }

        if (message.method && message.method == "broadcast" && message.data) {
          this.data = message.data
        }
        // this.changeDetectorRef.detectChanges();
      },
      error: (error) => {
        console.error("Websocket error: ", error)
        this.connectWebsocket()
      },
      complete: () => {
        console.log("WebSocket connection closed")
        this.connectWebsocket()
      }
    }
    )
  }

  changeView(view: string): void {
    if (this._possibleCurrentTab.includes(view)) {
      this.currentTab = view;
    }
  }

  getData(): void {
    let payload = {
      'method': 'get',
      'type': 'data',
    }
    this.webSocketService.send(payload);
  }
  getSchemas(): void {
    let schemaPayload = {
      'method': 'get',
      'type': 'schema',
    }
    this.webSocketService.send(schemaPayload);
  }

  changeOrCreateEvent(event: object): void {
    console.log("Tritter new SmartHomeeventwith ", event)
    this.webSocketService.send(event);
  }

}
