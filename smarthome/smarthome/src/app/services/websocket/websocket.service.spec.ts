import { TestBed } from '@angular/core/testing';

import { webSocketService } from './websocket.service';

describe('WebsocketService', () => {
  let service: webSocketService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(webSocketService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
