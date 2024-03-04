import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdaptUIViewComponent } from './adapt-uiview.component';

describe('AdaptUIViewComponent', () => {
  let component: AdaptUIViewComponent;
  let fixture: ComponentFixture<AdaptUIViewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdaptUIViewComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdaptUIViewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
