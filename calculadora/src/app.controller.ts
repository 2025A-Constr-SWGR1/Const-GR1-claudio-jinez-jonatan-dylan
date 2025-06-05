<<<<<<< HEAD
<<<<<<< HEAD
import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }
}
=======
=======
>>>>>>> 6c3af48c2a4d0ae3b4fc657cd5be8d174cf28bf9
import { Controller, Get } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
  constructor(private readonly appService: AppService) {}

  @Get()
  getHello(): string {
    return this.appService.getHello();
  }
}
<<<<<<< HEAD
>>>>>>> 6c3af48 (Subiendo todos los archivos desde la nueva computadora)
=======
>>>>>>> 6c3af48c2a4d0ae3b4fc657cd5be8d174cf28bf9
